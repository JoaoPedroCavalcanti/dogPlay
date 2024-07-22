import random
from datetime import datetime, timedelta

def generate_random_date_time():
    # Generate a random date
    start_date = datetime(1900, 1, 1)
    end_date = datetime(2100, 12, 31)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    
    # Format the date as DD/MM/YYYY
    formatted_date = random_date.strftime('%d/%m/%Y')
    
    # Generate a random hour with minutes set to 00
    random_hour = random.randint(0, 23)
    formatted_time = f"{random_hour:02}:00"
    
    # Save in a dictionary
    result = {
        'date': formatted_date,
        'time': formatted_time
    }
    
    return result

# Example usage
# print(random_date_time)
# random_date_time = generate_random_date_time()
# print(random_date_time['time'])

# print(random_date_time['date'])

def gerar_lorem_ipsum(num_palavras=1):
    palavras_lorem = [
        'lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 
        'elit', 'sed', 'do', 'eiusmod', 'tempor', 'incididunt', 'ut', 'labore',
        'et', 'dolore', 'magna', 'aliqua', 'enim', 'ad', 'minim', 'veniam'
    ]
    
    # Garantir que num_palavras não seja maior que o número de palavras disponíveis
    num_palavras = min(num_palavras, len(palavras_lorem))
    
    # Escolher palavras aleatórias
    palavras_selecionadas = random.sample(palavras_lorem, num_palavras)
    
    # Retornar as palavras como uma string
    return ' '.join(palavras_selecionadas)

# Exemplos de uso
# print(gerar_lorem_ipsum(1))  # Retorna uma palavra Lorem Ipsum
# print(gerar_lorem_ipsum(2))  # Retorna duas palavras Lorem Ipsum

def generate_random_data():
    tempDateTime = generate_random_date_time()
    result = {
        'name': gerar_lorem_ipsum(2),
        'dogName': gerar_lorem_ipsum(1),
        'checkIn': tempDateTime['time'],
        'checkOut': '22:00',
        'date': tempDateTime['date']
    }
    return result

# a = generate_random_data()
# print(a)
    