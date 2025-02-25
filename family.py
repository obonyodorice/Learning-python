def family():
    favourite={}

    while True:

        
        also=input('Do you wanna continue (y/n)')

        if also=='n':
           break
        
        elif also == 'y':
            name=input('Enter your name:')
            colour=input('Whats your favourite colour:')
            favourite[name] = colour
        # else:
        #    continue

        
    
    for key, value in favourite.items():
         print(f'{key}:{value}')

family()

