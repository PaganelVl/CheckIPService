from ip2geotools.databases.noncommercial import DbIpCity
from rich.console import Console
from rich.table import Table


def main():
    ip = input("Enter IP: ")

    data = DbIpCity.get(ip)

    if data.region == "Donetsk":
        data.country = "DPR"
    elif data.region == "Lugansk":
        data.country = "LPR"

    console = Console()

    table = Table(show_header=True, style="blue")
    table.add_column("Parameter", style="cyan")
    table.add_column("Value", style="red")
    table.add_row("IP", ip)
    table.add_row("City", data.city)
    table.add_row("Region", data.region)
    table.add_row("Country", data.country)
    table.add_row("Latitude", f"{str(data.latitude)}°")
    table.add_row("Longitude", f"{str(data.longitude)}°")

    console.print(table, justify="center")


if __name__ == "__main__":
    main()
