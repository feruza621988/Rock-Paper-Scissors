#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random

def player(prev_play, opponent_history=[]):
    # opponent_history ga raqibning oldingi harakatlarini qo'shish
    if prev_play != "":
        opponent_history.append(prev_play)

    # Agar opponent_history bo'sh bo'lsa, tasodifiy harakat tanlash
    if not opponent_history:
        return random.choice(["R", "P", "S"])

    # Raqibning oxirgi harakatini aniqlab, unga qarshi mos javob berish
    last_move = opponent_history[-1]
    
    # O'yin naqshini aniqlash va javobni qaytarish
    if last_move == "R":
        return "P"  # "Rock"ga qarshi "Paper"ni tanlash
    elif last_move == "P":
        return "S"  # "Paper"ga qarshi "Scissors"ni tanlash
    else:
        return "R"  # "Scissors"ga qarshi "Rock"ni tanlash


# In[4]:


from RPS_game import play, quincy  # quincy - sinov botlaridan biri

# O'zingizning 'player' funksiyangizni quincy botiga qarshi sinab ko'rish
play(player, quincy, 1000, verbose=True)


# In[ ]:




