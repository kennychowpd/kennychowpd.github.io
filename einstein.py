def main():
    mass = int(input("mass(in kg): "))
    joule = m_j_conversion(mass)
    print(f"According to Albert Einstein, {mass}kg of mass equals {joule} of Joules.")
    
    
def m_j_conversion(mass):
    j = mass * 300000000 ** 2
    return j

main()