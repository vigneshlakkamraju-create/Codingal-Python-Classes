class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.songs = []
        print(f"Playlist '{self.name}' ([self.genre]) is ready!")


    def add_song(self, song):
        self.songs.append(song)
        print(f"'[song]' added to playlist '{self.name}'.")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"'{song}' removed from playlist '{self.name}'.")
        else:
            print(f"'{song} ({self.genre})' is not in the playlist.")

    def display(self):
            print(f"\n ---- {self.name} ({self.genre}) ----")
            if self.songs:
                for i, song in enumerate(self.songs, 1):
                    print(f"{i}. {song}")
            else:
                print("No songs in the playlist yet. Add some")

    def _del__(self):
        print(f"Playlist '{self.name}' is being deleted.")

my_playlist = Playlist("Road Trip Mix", "Pop")

while True:
    print("\n1. Add a song 2. Remove a song 3. Display playlist 4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        song = input("Enter the song name: ")
        my_playlist.add_song(song)
    elif choice == "2":
        song = input("Enter the song name to remove: ")
        my_playlist.remove_song(song)
    elif choice == "3":
        my_playlist.display()
    elif choice == "4":
        del my_playlist
        break
    else:
        print("Invalid choice. Enter 1, 2, 3, or 4.")

        