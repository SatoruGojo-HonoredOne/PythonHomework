print("Hello Anay!")
question = input("Are you solving for work, power, acceleration, force, velocity, or initial velocity?")
if question == "work":
    force = float(input("What is the force?"))
    distance = float(input("What is the distance?"))
    work = force * distance
    print(f"The work done is {work} Joules.")
if question == "power":
    work = float(input("What is the work?"))
    time = float(input("What is the time?"))
    power = work / time
    print(f"The power is {power} Watts.")
if question == "acceleration":
    final_velocity = float(input("What is the final velocity?"))
    initial_velocity = float(input("What is the initial velocity?"))
    time = float(input("What is the time?"))
    acceleration = (final_velocity - initial_velocity) / time
    print(f"The acceleration is {acceleration} m/s^2.")
if question == "force":
    mass = float(input("What is the mass?"))
    acceleration = float(input("What is the acceleration?"))
    force = mass * acceleration
    print(f"The force is {force} Newtons.")
if question == "velocity":
    distance = float(input("What is the distance?"))
    time = float(input("What is the time?"))
    velocity = distance / time
    print(f"The velocity is {velocity} m/s.")
if question == "initial velocity":
    final_velocity = float(input("What is the final velocity?"))
    acceleration = float(input("What is the acceleration?"))
    time = float(input("What is the time?"))
    initial_velocity = final_velocity - (acceleration * time)
    print(f"The initial velocity is {initial_velocity} m/s.")
