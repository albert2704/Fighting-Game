# Updated code for `fighter.py` to add mana functionality and abilities
# fighter_updated_code = 
class Fighter:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.mana = 100  # Initialize mana to 100

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {amount} damage, health is now {self.health}.")

    def gain_mana(self, amount):
        self.mana += amount
        if self.mana > 100:
            self.mana = 100
        print(f"{self.name} gains {amount} mana, mana is now {self.mana}.")

    def use_mana(self, amount):
        if self.mana >= amount:
            self.mana -= amount
            print(f"{self.name} uses {amount} mana, mana is now {self.mana}.")
            return True
        else:
            print(f"{self.name} Không đủ mana.")
            return False

    # Abilities o and t - consume 20 mana each
    def ability_o(self):
        if self.use_mana(20):
            print(f"{self.name} uses ability 'o'.")
            # Add ability-specific behavior here (e.g., damage to opponent)

    def ability_t(self):
        if self.use_mana(20):
            print(f"{self.name} uses ability 't'.")
            # Add ability-specific behavior here

    # Abilities e, r, u, i - gain mana if they hit
    def ability_e(self, hit_successful):
        if hit_successful:
            self.gain_mana(10)
            print(f"{self.name} successfully hits with ability 'e'.")

    def ability_r(self, hit_successful):
        if hit_successful:
            self.gain_mana(5)
            print(f"{self.name} successfully hits with ability 'r'.")

    def ability_u(self, hit_successful):
        if hit_successful:
            self.gain_mana(10)
            print(f"{self.name} successfully hits with ability 'u'.")

    def ability_i(self, hit_successful):
        if hit_successful:
            self.gain_mana(5)
            print(f"{self.name} successfully hits with ability 'i'.")



# Updated code for `main.py` to test the Fighter abilities with mana
# main
from fighter import Fighter

# Initialize two fighters
fighter1 = Fighter("Warrior")
fighter2 = Fighter("Mage")

# Example moves with mana cost and regeneration on hit
fighter1.ability_o()  # Should consume 20 mana
fighter1.ability_t()  # Should consume another 20 mana

# Check abilities that regenerate mana on hit (assuming successful hits)
fighter1.ability_e(hit_successful=True)  # Should add 10 mana
fighter1.ability_r(hit_successful=True)  # Should add 5 mana
fighter1.ability_u(hit_successful=True)  # Should add 10 mana
fighter1.ability_i(hit_successful=True)  # Should add 5 mana

# Check mana and health status after some moves
print(f"Final status - {fighter1.name}: Health = {fighter1.health}, Mana = {fighter1.mana}")

