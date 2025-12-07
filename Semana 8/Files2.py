def read_songs(input_file):
    try:
        with open(input_file, 'r') as file:
            songs = [line.strip() for line in file]
        return songs
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
        return []

def order_songs(songs):
    return sorted(songs)

def save_songs(songs, output_file):
    try:
        with open(output_file, 'w') as file:
            for song in songs:
                file.write(song + '\n')
        print(f"Songs saved {len(songs)} to '{output_file}'.")
    except Exception as e:
        print(f"An error occurred while saving songs: {e}")

def main():
    input_file = 'newfile.txt'
    output_file = 'newfile1.txt'

    songs = read_songs(input_file)
    if songs:
        songs_ordered = order_songs(songs)
        #print(songs_ordered)
        for song in songs_ordered:
            print(song)
        save_songs(songs_ordered, output_file)

if __name__ == "__main__":
    main()


