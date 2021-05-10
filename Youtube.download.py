from pytube import YouTube
while True:
    url = str(input('Qual o link do youtube? '))
    video = YouTube(url)
    try:
        print(video.title)
    except Exception():
        print("Não foi possivel obter o link")
    else:
        print('''Digite 1 para exibir o titulo":
        Digite 2 para exibir mais informações}
        Digite 3 para fazer download"''')
        numero = int(input('Qual a sua escolha: '))
        if numero == 1:
            print(video.title)
        if numero == 2:
            print(f'{video.views} pessoas vizualiram o video')
            print(f'{video.rating} foi a media avaliada')
            print(f'{video.publish_date}. Esta é a data de publicação')
            print(f'{video.age_restricted}.Esta é a idade mínima')
        if numero == 3:
            qualidade= video.streams.get_highest_resolution()
            qualidade.download()
            print('Fazendo o download')
    escolha = str(input('Deseja finalizar? ').strip().upper()[0])
    if escolha == 'S':
        break
