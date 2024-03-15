from pytube import YouTube, Playlist

def download_video(url, format='mp4'):
    try:
        yt = YouTube(url)
        if format == 'mp4':
            video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        elif format == 'mp3':
            video = yt.streams.filter(only_audio=True).first()
        else:
            print("Formato de download não suportado.")
            return

        if video:
            video.download()
            print("Download concluído!")
        else:
            print("Nenhuma stream de vídeo encontrada.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def download_playlist(url, format='mp4'):
    try:
        playlist = Playlist(url)
        for video_url in playlist.video_urls:
            download_video(video_url, format)
    except Exception as e:
        print(f"Ocorreu um erro ao baixar a playlist: {e}")

def main():
    while True:
        print("Escolha uma opção:")
        print("1. Baixar vídeo individual")
        print("2. Baixar playlist")
        print("3. Sair")

        choice = input("Insira o número da opção desejada: ")

        if choice == '1':
            video_url = input("Insira o link do vídeo do YouTube: ")
            format = input("Escolha o formato de download (mp3 ou mp4): ")
            if format not in ['mp3', 'mp4']:
                print("Formato de download não suportado.")
            else:
                download_video(video_url, format)
        elif choice == '2':
            playlist_url = input("Insira o link da playlist do YouTube: ")
            format = input("Escolha o formato de download (mp3 ou mp4): ")
            if format not in ['mp3', 'mp4']:
                print("Formato de download não suportado.")
            else:
                download_playlist(playlist_url, format)
        elif choice == '3':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
