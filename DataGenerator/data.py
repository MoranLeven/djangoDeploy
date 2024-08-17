import random
firstname_list = [
    "Aaron", "Abigail", "Adam", "Aiden", "Alex", "Alexander", "Alexis", "Alice", "Alicia", "Allison",
    "Alyssa", "Amelia", "Andrew", "Angela", "Anna", "Anthony", "Ashley", "Austin", "Ava", "Bailey",
    "Barbara", "Benjamin", "Blake", "Brandon", "Brayden", "Brian", "Brianna", "Brittany", "Brody", "Brooklyn",
    "Caleb", "Cameron", "Carlos", "Caroline", "Carter", "Charles", "Charlotte", "Chase", "Chloe", "Christian",
    "Christopher", "Claire", "Cole", "Colin", "Connor", "Cooper", "Daniel", "David", "Delilah", "Derek",
    "Destiny", "Devin","Colin", "Collin", "Conner", "Connor", "Cooper", "Coraline", "Cora", "Courtney",
    "Cruz", "Cynthia", "Daisy", "Dakota", "Dallas", "Damian", "Daniel", "Daniela", "Daniella", "Danielle",
    "Daphne", "David", "Dawson", "Delaney", "Delilah", "Demi", "Derek", "Desmond", "Destiny", "Devin",
    "Diego", "Dillon", "Dimitri", "Dominic", "Dominique", "Drew", "Dylan", "Easton", "Eden", "Edgar",
    "Edward", "Edwin", "Eleanor", "Elena", "Eliana", "Elijah", "Elisa", "Elise", "Eliza", "Elizabeth",
    "Ella", "Ellie", "Elliot", "Elliott", "Eloise", "Elsa", "Ember", "Emerson", "Emery", "Emilia",
    "Emiliano", "Emily", "Emma", "Emmanuel", "Emmett", "Enzo", "Eric", "Erick", "Erin", "Esme",
    "Esperanza", "Ethan", "Eva", "Evan", "Everett", "Evelyn", "Ezequiel", "Ezra", "Faith", "Fatima",
    "Felicity", "Felix", "Finley", "Finn", "Fiona", "Francisco", "Frank", "Franklin", "Gabriel", "Gabriella",
    "Gabrielle", "Ganesh"]

lastname_list = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
    "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts",
    "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes",
    "Stewart", "Morris", "Morales", "Murphy", "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper",
    "Peterson", "Bailey", "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson",
    "Watson", "Brooks", "Chavez", "Wood", "James", "Bennett", "Gray", "Mendoza", "Ruiz", "Hughes",
    "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers", "Long", "Ross", "Foster", "Jimenez"
]

domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "aol.com"]




# Sample data for bio generation
occupations = [
    "Software Developer 💻", "Graphic Designer 🎨", "Digital Marketer 📈", "Teacher 📚", "Data Scientist 📊",
    "Content Writer ✍️", "Photographer 📷", "Entrepreneur 🚀", "Product Manager 📦", "UX/UI Designer 🖥️",
    "Financial Analyst 💰", "Researcher 🔬", "Sales Executive 💼", "HR Manager 👥", "Consultant 💡"
]

hobbies = [
    "traveling ✈️", "reading 📖", "cooking 🍳", "photography 📸", "hiking 🥾", "gaming 🎮",
    "blogging 📝", "painting 🎨", "playing guitar 🎸", "yoga 🧘", "running 🏃", "gardening 🌱",
    "cycling 🚴", "dancing 💃", "writing ✍️", "watching movies 🎥", "volunteering 🤝"
]

traits = [
    "passionate ❤️", "creative 🎨", "dedicated 🔥", "curious 🧐", "adventurous 🌍",
    "friendly 😊", "motivated 🚀", "innovative 💡", "strategic 🧠", "problem solver 🛠️",
    "detail-oriented 🔍", "collaborative 🤝", "ambitious 🚀", "empathetic 🤗", "organized 📅"
]

bloodGroup_list = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-","NOTA"]


# Generate random bios
def generateBio():
    occupation = random.choice(occupations)
    hobby1 = random.choice(hobbies)
    hobby2 = random.choice(hobbies)
    while hobby1 == hobby2:  # Ensure hobbies are not the same
        hobby2 = random.choice(hobbies)
    trait = random.choice(traits)

    bio = f"A {trait} {occupation} who loves {hobby1} and {hobby2}."
    return bio

def generateBloodGroup():
    bg = random.choice(bloodGroup_list)
    return bg.lower() if bg != "NOTA" else bg

def generateHeight():
    return random.randint(50,300)

def generateWeight():
    return random.randint(20,400)


def generatePermissionLevel():
    return random.choice([1111,1110,1100,1000,0000,])

def generateGender():
    return random.choice(["Male","Female","Nahi Batana"])

def generateAge():
    return random.randint(18,130)

def generateEmail():
    first = random.choice(firstname_list).lower()
    last = random.choice(lastname_list).lower()
    domain = random.choice(domains)
    email = f"{first}.{last}@{domain}"
    return email


def generateNames():
    firstname =  random.choice(firstname_list)
    lastname =  random.choice(lastname_list)
    return {
            "username":firstname[:2]+lastname,
            "firstname": firstname,
            "lastname":lastname,
            "nickname":lastname[:2]+firstname[:2]
        }