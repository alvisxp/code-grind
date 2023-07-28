songs_in_playlist = int(input())
songs = list(map(int, input().split()))

playlist_dict = {}

for song in songs:
    if song in playlist_dict:
        playlist_dict[song] += 1
    else:
        playlist_dict[song] = 1

max_count = max(playlist_dict.values())

fav_singers = sum(count == max_count for count in playlist_dict.values())
print(fav_singers)
