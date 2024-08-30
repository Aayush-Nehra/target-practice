class Settings:
    def __init__(self) -> None:
        #Screen Settings
        self.screen_width = 900
        self.screen_height = 700
        self.bg_color = (0, 0, 0)

        #Bullet Settings
        self.bullet_width = 20
        self.bullet_height = 5
        self.bullet_color = (255, 0, 0)
        self.level_scaling = 1.2

        #Game Settings
        self.max_missed = 3
        self.hits_for_level_up = 5

        self.initialize_dynamic_settings()

        

    def initialize_dynamic_settings(self):
        #Target Settings
        self.target_speed = 3.0

        #Shooter Settings
        self.shooter_speed = 1.0

        # Bullet Settings
        self.bullet_speed = 10.0

    def increase_game_speed(self):
        self.target_speed *= self.level_scaling
        self.shooter_speed *= self.level_scaling
        self.bullet_speed *= self.level_scaling