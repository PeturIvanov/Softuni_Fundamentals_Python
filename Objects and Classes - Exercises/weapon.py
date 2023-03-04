class Weapon:

    def __init__(self, bullets: int):
        self.bullets = bullets

    def shoot(self):
        init_bullets = self.bullets
        if init_bullets > 0:
            self.bullets -= 1
            return "shooting..."
        else:
            return "no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"
