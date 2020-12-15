import match_details
from pycricbuzz import Cricbuzz
import json
import websockets
import asyncio

async def on_message(websocket, path):
    message = await websocket.recv()
    message = json.loads(message)
    if (message["type"] == "get_matches"):
        api_instance = Cricbuzz()
        matches = api_instance.matches()
        await websocket.send(json.dumps(matches))
    elif (message["type"] == "match_id"):
        api_instance = Cricbuzz()
        match_info = match_details.get_match_info(api_instance, message["id"])
        livescore = match_details.get_live_score(api_instance, message["id"])
        json_object = json.dumps({"series": match_details.get_series_name(match_info),
                                    "team_names": match_details.get_team_names(match_info),
                                    "venue_names" : match_details.get_venue_name(match_info),
                                    "venue_location" : match_details.get_venue_location(match_info),
                                    "umpire" : match_details.get_umpire_name(match_info),
                                    "score" : {"runs": match_details.get_total_runs_of_batting_team(livescore),
                                                "wickets": match_details.get_total_wickets_of_batting_team(livescore),
                                                "overs" : match_details.get_total_overs(livescore),
                                                "inning" : match_details.get_inning_number(livescore),
                                                "batting_team" : match_details.get_batting_team_name(livescore),
                                                "bowling_team" : match_details.get_bowling_team_name(livescore),
                                                "batsman" : match_details.get_batsman(livescore),
                                                "bowler" : match_details.get_bowler(livescore)
                                            },
                                })
        await websocket.send(json_object)


if __name__ == '__main__':
    start_server = websockets.serve(on_message, "localhost", 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
