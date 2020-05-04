# flake8: noqa
import requests
import difflib

SEED = 31415

true_requests = {}

false_requests = []
# Response struct
# [
#     {
#         "text": "t1.",
#         "hypotheses": [
#             {
#                 "skill_name": "game_cooperative_skill",
#                 "text": "b1.",
#                 "confidence": 1.0,
#                 "can_continue": "can",
#                 "state": {"1": 2},
#             }
#         ],
#     },
#     {"text": "b1.", "active_skill": "game_cooperative_skill", "confidence": 1.0},
#     {"text": "t2.", "hypotheses": []},
# ]


def update_utterances(utterances=[], response=None, text_request=""):
    if response:
        text, confidence, attr = response
        can_continue = attr["can_continue"]
        state = attr["state"]
        utterances[-1]["hypotheses"] = [
            {
                "skill_name": "game_cooperative_skill",
                "text": text,
                "confidence": confidence,
                "can_continue": can_continue,
                "state": state,
            }
        ]
        utterances += [
            {"text": text, "orig_text": text, "active_skill": "game_cooperative_skill", "confidence": confidence},
        ]
    if text_request:
        utterances += [
            {"text": text_request, "hypotheses": []},
        ]
    return utterances


request_utters = [
    "hello",
    "top",
    "week",
    "yes",
    "ok",
    "top of month",
    "yes",
    "talk",
    "yes",
    "yes",
    "stop",
    "top of year",
    "yes",
    "yes",
    "say",
    "yes",
    "yes",
    "no",
    "awful",
    "next",
    "next",
    "next",
    "stop",
    "top",
    "no",
    "stop",
    "top of last month",
    "yes",
    "tell me about top of last year",
    "stop",
    "i wanna",
    "sure",
    "last year",
    "sure",
    "next",
    "next",
    "next",
    "next",
    "next",
    "next",
    "next",
    "next",
    "next",
    "next",
    "next",
    "next",
    "next",
    "next",
    "next",
    "next",
    "next",
    "next",
    "next",
]

true_response_utters = [
    "I like to talk about games. Got a list of the top released games, wanna discuss it? Say tell me about the best games",
    "I can tell you about popular games. For now, I can talk about the most popular games for this or last year , last month, or even the last week (hotties!). Which of these time periods is of interest for you?",
    " There was 1 newly released game highly rated in the last week. Do you want to learn more? ",
    "The game with the highest rating is Final Fantasy VII Remake. It was released on April 10 2020. It's a combination of Action Adventure & RPG. 90 percent of people marked Final Fantasy VII Remake as exceptional.  These are all the games from the past week.  If you want to discuss it in details say I want to talk about it.  Otherwise we can always talk about other things.",
    "I like to talk about games. Got a list of the top released games, wanna discuss it? Say tell me about the best games",
    " There was 1 newly released game highly rated in the last month. Do you want to learn more? ",
    "The game with the highest rating is Final Fantasy VII Remake. It was released on April 10 2020. It's a combination of Action Adventure & RPG. 90 percent of people marked Final Fantasy VII Remake as exceptional.  These are all the games from the past month.  If you want to discuss it in details say I want to talk about it.  Otherwise we can always talk about other things.",
    "Do you want to talk in more detail about the game called Final Fantasy VII Remake?",
    "Have you played it before? ",
    "So I suppose you liked Final Fantasy VII Remake right? How would you rate the desire to play it again, from 1 to 10?",
    "OK, I won’t continue, but if you want to talk about the best games, Say tell me about the coolest games",
    " There were 18 newly released games highly rated in this year. Do you want to learn more? ",
    "The game with the highest rating is Dota Underlords. It was released on February 25 2020. It's a combination of Strategy Board Games & Casual. 44 percent of people marked Dota Underlords as recommended.  If you want to discuss it in details say I want to talk about it.  Do you want to learn more about it, or shall we move on? ",
    "The next game is Black Mesa. It was released on March 06 2020. It's a combination of  Shooter & Indie. 46 percent of people marked Black Mesa as exceptional.  Wanna hear more about it or the next one? ",
    "Do you want to talk in more detail about the game called Black Mesa?",
    "Have you played it before? ",
    "So I suppose you liked Black Mesa right? How would you rate the desire to play it again, from 1 to 10?",
    "I didn't get what you've just said. I asked what rating would you give Black Mesa. For example, you can say: one or ten  or any number from 1 to 10. Or do you want to stop for now?",
    "You gave it a super low rating. Your rating is way lower than one given by the rest of the players. Most of them rated it at 8.6 points. My bad. My memory failed me and I can't recall anything else about the games. Just ratings. But I promise to fix my memory card and get back to you. In the meanwhile, do you want to discuss the next game?",
    "The next game is Besiege. It was released on February 18 2020. It's a combination of Strategy Simulation & Indie. 66 percent of people marked Besiege as recommended.  Wanna hear more about it or the next one? ",
    "The next game is DOOM Eternal. It was released on March 20 2020. It's a combination of  Action & Shooter. 58 percent of people marked DOOM Eternal as exceptional.  Let me know if we should talk about the next one or discuss this one ",
    "The next game is Ori and the Will of the Wisps. It was released on March 11 2020. It's a combination of  Adventure & Platformer. 67 percent of people marked Ori and the Will of the Wisps as exceptional.  Chatting about it or the next one? ",
    "OK, I won’t continue, but if you want to talk about the best games, Say tell me about the coolest games",
    "Last time we talked about the best games of this year. For now, I can talk about the most popular games for this or last year , last month, or even the last week (hotties!). Which of these time periods is of interest for you?",
    "You can always talk to me about other popular games. What do you want to talk about?",
    "OK, I won’t continue, but if you want to talk about the best games, Say tell me about the coolest games",
    " There was 1 newly released game highly rated in the last month. Do you want to learn more? ",
    "The game with the highest rating is Final Fantasy VII Remake. It was released on April 10 2020. It's a combination of Action Adventure & RPG. 90 percent of people marked Final Fantasy VII Remake as exceptional.  These are all the games from the past month.  If you want to discuss it in details say I want to talk about it.  Otherwise we can always talk about other things.",
    " There were 19 newly released games highly rated in the last year. Do you want to learn more? ",
    "OK, I won’t continue, but if you want to talk about the best games, Say tell me about the coolest games",
    "Last time we talked about the best games of last year. For now, I can talk about the most popular games for this or last year , last month, or even the last week (hotties!). Which of these time periods is of interest for you?",
    "I didn't get what you've just said. Do you want to talk about the best games of the past year, this year, last month or week? For example, you can say: show me the best games of this year. Or do you want to stop for now? ",
    " There were 19 newly released games highly rated in the last year. Do you want to learn more? ",
    "The game with the highest rating is Death Stranding. It was released on November 08 2019. It's a combination of Action Shooter & Adventure. 65 percent of people marked Death Stranding as exceptional.  If you want to discuss it in details say I want to talk about it.  Discussing it or moving on? ",
    "The next game is Sekiro: Shadows Die Twice. It was released on March 22 2019. It's a combination of  Action & RPG. 59 percent of people marked Sekiro: Shadows Die Twice as exceptional.  Let me know if we should talk about the next one or discuss this one ",
    "The next game is Apex Legends. It was released on February 04 2019. It's a combination of Action Shooter & Massively Multiplayer. 50 percent of people marked Apex Legends as recommended.  Wanna hear more about it or the next one? ",
    "The next game is Borderlands Game of the Year Enhanced. It was released on April 03 2019. It's a combination of Action Shooter & RPG. 57 percent of people marked Borderlands Game of the Year Enhanced as recommended.  Chatting about it or the next one? ",
    "The next game is Star Wars Jedi: Fallen Order. It was released on November 15 2019. It's a combination of  Action & Adventure. 54 percent of people marked Star Wars Jedi: Fallen Order as recommended.  Discussing it or moving on? ",
    "The next game is Minion Masters. It was released on May 24 2019. It's a combination of Action Strategy & Indie. 39 percent of people marked Minion Masters as skip.  Chatting about it or the next one? ",
    "The next game is Resident Evil 2. It was released on January 25 2019. It's a combination of Action Shooter & Adventure. 63 percent of people marked Resident Evil 2 as exceptional.  Discussing it or moving on? ",
    "The next game is The Outer Worlds. It was released on October 25 2019. It's RPG. 56 percent of people marked The Outer Worlds as recommended.  Let me know if we should talk about the next one or discuss this one ",
    "The next game is Metro Exodus. It was released on February 15 2019. It's a combination of  Action & Shooter. 44 percent of people marked Metro Exodus as recommended.  Do you want to learn more about it, or shall we move on? ",
    "The next game is Gothic Playable Teaser. It was released on December 14 2019. It's RPG. 41 percent of people marked Gothic Playable Teaser as recommended.  Do you want to learn more about it, or shall we move on? ",
    "The next game is Control. It was released on August 27 2019. It's a combination of Action Shooter & Adventure. 44 percent of people marked Control as recommended.  Discussing it or moving on? ",
    "The next game is Gears 5. It was released on September 10 2019. It's a combination of  Action & Shooter. 61 percent of people marked Gears 5 as recommended.  Let me know if we should talk about the next one or discuss this one ",
    "The next game is Slay the Spire. It was released on January 22 2019. It's a combination of Strategy Card & Indie. 52 percent of people marked Slay the Spire as exceptional.  Talking about it or going on? ",
    "The next game is Days Gone. It was released on April 26 2019. It's a combination of  Action & Adventure. 51 percent of people marked Days Gone as recommended.  Talking about it or going on? ",
    "The next game is A Plague Tale: Innocence. It was released on May 13 2019. It's a combination of  Action & Adventure. 45 percent of people marked A Plague Tale: Innocence as recommended.  Discussing it or moving on? ",
    "The next game is Mortal Kombat 11. It was released on April 23 2019. It's a combination of Action Adventure & Fighting. 57 percent of people marked Mortal Kombat 11 as recommended.  Talking about it or going on? ",
    "The next game is Tom Clancy’s The Division 2. It was released on March 15 2019. It's a combination of Action, Shooter Adventure & RPG. 58 percent of people marked Tom Clancy’s The Division 2 as recommended.  Do you want to learn more about it, or shall we move on? ",
    "The next game is Borderlands 3. It was released on September 13 2019. It's a combination of Action Shooter & Adventure. 46 percent of people marked Borderlands 3 as recommended.  Let me know if we should talk about the next one or discuss this one ",
    "The next game is Kingdom Hearts III. It was released on January 29 2019. It's a combination of Action Adventure & RPG. 49 percent of people marked Kingdom Hearts III as recommended.  These are all the games from last year.  If you want to discuss it in details say I want to talk about it.  Otherwise we can always talk about other things.",
    "Sorry",
]


def test_skill():
    url = "http://0.0.0.0:8068/respond"
    utterances = []
    warnings = 0
    for ind, (req_utter, true_resp_utter) in enumerate(zip(request_utters, true_response_utters)):
        utterances = update_utterances(utterances=utterances, text_request=req_utter)
        human_utterances = [uttr for uttr in utterances if "hypotheses" in uttr]
        input_data = {"dialogs": [{"utterances": utterances, "human_utterances": human_utterances}]}
        input_data["rand_seed"] = SEED + ind
        response = requests.post(url, json=input_data).json()[0]
        utterances = update_utterances(utterances=utterances, response=response)
        text, confidence, attr = response
        if difflib.SequenceMatcher(None, true_resp_utter.split(), text.split()).ratio() != 1.0:
            print("----------------------------------------")
            print(f"req_utter = {req_utter}")
            print(f"true_resp_utter = {true_resp_utter}")
            print(f"cand_resp_utter = {text}")
        # elif difflib.SequenceMatcher(None, true_resp_utter.split(), text.split()).ratio() < 0.4:
            warnings += 1
        print(difflib.SequenceMatcher(None, true_resp_utter.split(), text.split()).ratio())
    assert warnings == 0
    print("SUCCESS!")


if __name__ == "__main__":
    test_skill()
