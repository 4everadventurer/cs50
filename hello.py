SHOWS= ["seri", "jaeyoung", "Jiwon", "jihooN"]

def main():
    cleaned_shows=[]
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())

    print(', '.join(cleaned_shows))    
main()     