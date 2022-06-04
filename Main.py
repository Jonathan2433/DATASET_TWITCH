import csv
import traceback
import re

# ouverture et transformation du fichier en list
def open_file(file):
    file = open(file, "r")
    reader = csv.reader(file)
    data = list(reader)
    file.close()
    return data[1:]

def real_streams(data):
    real_streams = []
    for row in data:
        try:
            minutes_streamed = float(row[13])
            if minutes_streamed != 0:
                # isolation du nombre de stream
                real_streams.append(row)
        except Exception:
            print("Probleme lors de la conversion en Integer !", str(Exception), str(traceback.print_exc()))
    return real_streams

def average_viewers_total(data):
    total_average_viewers = 0
    for stream in data:
        try:
            average_viewers = float(stream[3])
            # cumul des viewers moyen
            total_average_viewers += average_viewers
        except Exception:
            print("Probleme lors de la conversion en Float !", str(Exception), str(traceback.print_exc()))
    return total_average_viewers

def unique_viewers_total(data):
    total_unique_viewers = 0
    for stream in data:
        try:
            minutes_streamed = float(stream[13])
            # verification si il y as bien eu un live
            if minutes_streamed != 0:
                unique_viewers = int(stream[14])
                # cumul des viewers unique
                total_unique_viewers += unique_viewers
        except Exception:
            print("Probleme lors de la conversion en Integer !", str(Exception), str(traceback.print_exc()))
    return total_unique_viewers

def display_data(data):
    month_data = []
    for i, stream in enumerate(data):
        streams = real_streams(stream)
        monday_streams = []
        #isolement des streams du lundi soir
        if re.match("^[Mon]", streams[0][0]):
            monday_streams.append(streams)
            # nombre de stream le lundi soir durant le mois
            total_streams_monday = len(monday_streams)
            # nombre total de viewers moyen sur les lundis durant le mois
            total_average_viewers_monday = average_viewers_total(monday_streams)
            # viewers moyen le lundi sur le mois
            average_viewers_monday = total_average_viewers_monday / total_streams_monday
            # nombre total de viewers unique le lundi sur le mois
            total_unique_viewers_monday = unique_viewers_total(monday_streams)
        # nombre de stream durant le mois
        total_streams_month = len(streams)
        # nombre total de viewers moyen sur le mois
        total_average_viewers_month = average_viewers_total(streams)
        # viewers moyen sur le mois
        average_viewers_month = total_average_viewers_month / total_streams_month
        # nombre total de viewers unique sur le mois
        total_unique_viewers_month = unique_viewers_total(streams)
        # todo
        # return result for monday stream
        month_data.extend(["fichier numéro : " +str(i +1) , str(average_viewers_month) + ", Viewers moyen, et, " + str(total_unique_viewers_month) + ", Viewers unique pour, " + str(total_streams_month) + ", Streams "])
    return



# enregistrement de mes data dans différentes variables
data_first_month = open_file("1er mois.csv")
data_second_month = open_file("2eme mois.csv")
data_third_month = open_file("3eme mois ( jusquau premier live tech.csv")
data_first_tech_month = open_file("1er mois tech.csv")
data_second_tech_month = open_file("2eme mois tech.csv")

data_all_month = [data_first_month, data_second_month, data_third_month, data_first_tech_month, data_second_tech_month]

infos = data_first_month[0]

display_data = display_data(data_all_month)

for month in display_data:
    print(month)
