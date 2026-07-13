is_raining = True
is_sunny = True
is_windy = False

if is_raining:
    print("Wear a raincoat and take an umbrella")
if is_sunny:
    print("Dress light and wear sunscreen")
if is_windy:
    print("Hold on to your hat")
elif not is_raining and not is_sunny and not is_windy:
    print("Do what makes sense")
