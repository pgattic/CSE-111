from sentences import *
import pytest

def test_get_determiner():
	for _ in range(4):
		assert get_determiner(1) in ["a", "one", "the"]
	for _ in range(4):
		assert get_determiner(2) in ["some", "many", "the"]

def test_get_noun():
	for _ in range(4):
		assert get_noun(1) in ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
	for _ in range(4):
		assert get_noun(2) in ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

def test_get_verb():
	for _ in range(4):
		assert get_verb(1, "past") in ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
	for _ in range(4):
		assert get_verb(1, "present") in ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
	for _ in range(4):
		assert get_verb(2, "present") in ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
	for _ in range(4):
		assert get_verb(2, "future") in ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

pytest.main(["-v", "--tb=line", "-rN", __file__])
