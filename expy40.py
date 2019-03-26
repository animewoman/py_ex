import forExpy40

forExpy40.apple()
print(forExpy40.tangerine)


class MyStuff(object):
    def __init__(self):
        self.tangerine = "Hello world"

    def apple(self):
        print("Hello World")


thing = MyStuff()
thing.apple()
print(thing.tangerine)


class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_b_day = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

happy_b_day.sing_me_a_song()
