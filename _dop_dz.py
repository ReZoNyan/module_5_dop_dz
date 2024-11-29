from time import sleep


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_pass(password)
        self.age = age

    def hash_pass(self, password):
        return hash(password)

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return f'Пользователь: {self.nickname}, возраст: {self.age}'


class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Название: {self.title}, продолжительность: {self.duration}, ограничение по возрасту: {self.adult_mode}'

    def __eq__(self, other):
        return self.title == other.title


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Такой пользователь: {nickname}, уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and user.password == self.hash_pass(password):
                self.current_user = user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for arg in args:
            if arg not in self.videos:
                self.videos.append(arg)

    def get_videos(self, search):
        search = search.lower()
        list_search = []
        for video in self.videos:
            if search in video.title.lower():
                list_search.append(video.title)
        return list_search

    def watch_video(self, title):
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы посмотреть видео')
            return

        def get_v(title):
            for v in self.videos:
                if v.title == title:
                    video = v
                    return video

        video = get_v(title)
        if not video:
            print('Видео не найдено')
            return

        if video.adult_mode and self.current_user.age < 18:
            print('Вам нет 18, покиньте страницу')
            return

        for sec in range(video.time_now, video.duration):
            print(sec + 1, end=' ')
            sleep(1)

        video.time_now = 0
        print('конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Для чего девушкам парень программист?', 200)
v4 = Video('Для чего нужны программы?', 200)
ur.add(v1, v2, v3, v4)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')
