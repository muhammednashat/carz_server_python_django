import random
from products.models import CarModel


car_descriptions = [
    """A sleek sedan with modern design. 
Perfect for city driving. 
Offers comfort and efficiency.""",

    """A powerful SUV built for adventure. 
Spacious interior for family trips. 
Handles rough terrain with ease.""",

    """A compact hatchback with agile handling. 
Great for daily commutes. 
Fuel-efficient and stylish.""",

    """A luxury sports car with sharp curves. 
Delivers high speed performance. 
Crafted with premium materials.""",

    """An electric vehicle with long range. 
Quiet and eco-friendly. 
Equipped with smart technology.""",

    """A rugged pickup truck. 
Strong towing capacity. 
Durable and dependable.""",

    """A hybrid car that saves fuel. 
Smooth transitions between power modes. 
Ideal for eco-conscious drivers.""",

    """A convertible with open-top freedom. 
Perfect for sunny days. 
Sporty and elegant design.""",

    """A family van with huge capacity. 
Sliding doors for easy entry. 
Safe and reliable for kids.""",

    """A compact crossover SUV. 
Blends style and practicality. 
Good for both city and highway.""",
]

car_names = [
    "Toyota Corolla", "Honda Civic", "Ford Focus", "Chevrolet Malibu", "Nissan Altima",
    "Hyundai Elantra", "Kia Optima", "Volkswagen Jetta", "Subaru Impreza", "Mazda 3",
    "BMW 3 Series", "Mercedes C-Class", "Audi A4", "Lexus IS", "Acura TLX",
    "Infiniti Q50", "Tesla Model 3", "Volvo S60", "Jaguar XE", "Alfa Romeo Giulia",
    "Toyota Camry", "Honda Accord", "Ford Fusion", "Chevrolet Impala", "Nissan Maxima",
    "Hyundai Sonata", "Kia Stinger", "Volkswagen Passat", "Subaru Legacy", "Mazda 6",
    "BMW 5 Series", "Mercedes E-Class", "Audi A6", "Lexus ES", "Acura RLX",
    "Infiniti Q70", "Tesla Model S", "Volvo S90", "Jaguar XF", "Genesis G80",
    "Toyota Yaris", "Honda Fit", "Ford Fiesta", "Chevrolet Spark", "Nissan Versa",
    "Hyundai Accent", "Kia Rio", "Volkswagen Polo", "Mazda 2", "Suzuki Swift",
    "Toyota RAV4", "Honda CR-V", "Ford Escape", "Chevrolet Equinox", "Nissan Rogue",
    "Hyundai Tucson", "Kia Sportage", "Volkswagen Tiguan", "Subaru Forester", "Mazda CX-5",
    "BMW X3", "Mercedes GLC", "Audi Q5", "Lexus NX", "Acura RDX",
    "Infiniti QX50", "Tesla Model Y", "Volvo XC60", "Jaguar F-Pace", "Alfa Romeo Stelvio",
    "Toyota Highlander", "Honda Pilot", "Ford Explorer", "Chevrolet Traverse", "Nissan Pathfinder",
    "Hyundai Santa Fe", "Kia Sorento", "Volkswagen Atlas", "Subaru Ascent", "Mazda CX-9",
    "BMW X5", "Mercedes GLE", "Audi Q7", "Lexus RX", "Acura MDX",
    "Infiniti QX60", "Tesla Model X", "Volvo XC90", "Jaguar I-Pace", "Genesis GV80",
    "Toyota Land Cruiser", "Nissan Patrol", "Ford Expedition", "Chevrolet Tahoe", "Jeep Grand Cherokee",
    "GMC Yukon", "Cadillac Escalade", "Range Rover", "Mitsubishi Pajero", "Lincoln Navigator"
]
baseUrl = "https://raw.githubusercontent.com/muhammednashat/carz_images/main/"
counter = 99  
for i in range(115):
        counter +=  1 
        CarModel(
        imgUrl = f'{baseUrl}{counter}.png',
        name=random.choice(car_names),
        description=random.choice(car_descriptions),
        car_type=random.choice(list(CarModel.CarType)),
        fuel_type=random.choice(list(CarModel.FuelType)),
        brand=random.choice(list(CarModel.BrandCar)),
        transmission_options=random.choice(list(CarModel.TransmissionOptions)),
        is_trend=random.choice([True, False]),
        is_popular=random.choice([True, False]),
        can_connect_bluetooth=random.choice([True, False]),
        is_automatic=random.choice([True, False]),
        price=random.randint(1000, 50000),
        rating=random.randint(1, 5),
    ).save()

print('......... DONE.......................')