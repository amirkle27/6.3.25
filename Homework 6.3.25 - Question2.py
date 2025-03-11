


class EmojiImage:
    def __init__(self, file_name:str):
        self.file_name = file_name

    def __repr__(self):
        return f"EmojiImage({self.file_name})"


class EmojiImageFactory:
    _images = {}

    @staticmethod
    def get_image(file_name:str):
        if file_name not in EmojiImageFactory._images:
            EmojiImageFactory._images[file_name] = EmojiImage(file_name)
        return EmojiImageFactory._images[file_name]

class Emoji:
    def __init__(self, name:str, size:int, file_name):
        self.name = name
        self.size = size
        self.image = EmojiImageFactory.get_image(file_name)

    def __str__(self):
        return f"{self.name} Emoji (name = {self.name}, size = {self.size}, image = {self.image.file_name})"


emoji1 = Emoji("Smiley", 32, "smiley.png")
emoji2 = Emoji("Smiley", 64, "smiley.png")
emoji3 = Emoji("Heart", 32, "heart.png")
emoji4 = Emoji("Heart", 64, "heart.png")
emoji5 = Emoji("ThumbsUp", 32, "thumbsup.png")
emoji6 = Emoji("ThumbsUp", 64, "thumbsup.png")

print(emoji1)
print(emoji2)
print(emoji3)
print(emoji4)
print(emoji5)
print(emoji6)
print("Number of unique images in memory:", len(EmojiImageFactory._images))

print(repr(EmojiImageFactory._images.values()))
