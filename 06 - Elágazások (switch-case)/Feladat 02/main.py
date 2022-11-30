honap: str = ""

print("Kérem adja meg a hónap nevét: ")

honap = input()

match honap:
    case "január" | "Január":
        print("1")
    case "február" | "Február":
        print(2)
    case "március" | "Március":
        print(3)
    case "április" | "Április":
        print(4)
    case "május" | "Május":
        print(5)
    case "június" | "Június":
        print(6)
    case "július" | "Július":
        print(7)
    case "augusztus" | "Augusztus":
        print(8)
    case "szeptember" | "Szeptember":
        print(9)
    case "október" | "Október":
        print(10)
    case "november" | "November":
        print(11)
    case "december" | "December":
        print(12)

        

