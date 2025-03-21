import os

def generate_invitations(template, attendees):
    # Vérifier que le modèle est une chaîne de caractères
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    # Vérifier que la liste des participants est une liste de dictionnaires
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Vérifier que le modèle n'est pas vide
    if not template:
        print("Error: Template is empty, no output files generated.")
        return

    # Vérifier que la liste des participants n'est pas vide
    if not attendees:
        print("Error: No data provided, no output files generated.")
        return

    # Itérer sur chaque participant et générer les fichiers
    for i, attendee in enumerate(attendees, start=1):
        # Remplacer les placeholders par les valeurs des participants
        # Si une valeur est manquante, remplacer par 'N/A'
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A")
        event_location = attendee.get("event_location", "N/A")

        # Remplacer dans le modèle
        invitation = template.format(name=name, event_title=event_title, event_date=event_date, event_location=event_location)

        # Générer le nom du fichier de sortie
        output_filename = f"output_{i}.txt"

        # Vérifier si le fichier existe déjà
        if os.path.exists(output_filename):
            print(f"Warning: {output_filename} already exists. It will be overwritten.")

        # Écrire dans le fichier de sortie
        try:
            with open(output_filename, 'w') as file:
                file.write(invitation)
            print(f"Invitation for {name} has been written to {output_filename}")
        except Exception as e:
            print(f"Error: Could not write to {output_filename}. {e}")

# Exemple d'utilisation dans un fichier principal (main)
if __name__ == "__main__":
    # Lire le modèle depuis un fichier
    try:
        with open('template.txt', 'r') as file:
            template_content = file.read()
    except FileNotFoundError:
        print("Error: template.txt not found.")
        exit(1)

    # Liste des participants
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    # Appeler la fonction avec le modèle et la liste des participants
    generate_invitations(template_content, attendees)
