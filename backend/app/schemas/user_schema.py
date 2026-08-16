from pydantic import BaseModel


class RegisterRequest(BaseModel):
    name: str
    first_name: str = ""
    last_name: str = ""
    email: str
    password: str
    role: str

    def model_post_init(self, __context):
        if self.name and not self.first_name and not self.last_name:
            parts = self.name.strip().split(" ", 1)
            self.first_name = parts[0]
            self.last_name = parts[1] if len(parts) > 1 else ""
        elif not self.name and self.first_name:
            self.name = f"{self.first_name} {self.last_name}".strip()
