#50weeks per year
#life until 90
lifetime_weeks = 50 * 90

def life_in_weeks():
    total_days_in_a_life = get_total_days_in_life()
    current_age_days = get_current_age_in_days(total_days_in_a_life)

    life_left = calc_how_much_left(current_age_days,total_days_in_a_life)

    print(F" YOU HAVE {life_left} days left on this planet!! (:<  .")


def get_total_days_in_life():
    lifetime_days = lifetime_weeks*7
    return lifetime_days

def get_current_age_in_days(lifetime_days):
    current_age = int(input("What is your age?"))
    return current_age

def calc_how_much_left(current_age_days,total_days_in_life):

    days_left = total_days_in_life-current_age_days
    return days_left

life_in_weeks()