class Task:
    def __init__(self, id, title, done=False) -> None:
        self.id = id
        self.title = title
        self.done = done

    def informations(self):
        return{
        "id": self.id,
        "title": self.title,
        "done": self.done
}
