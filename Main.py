import csv
import traceback

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
                real_streams.append(row)
        except Exception:
            print("Probleme lors de la conversion en Integer !", str(Exception), str(traceback.print_exc()))
    return real_streams

def average_viewers_total(data):
    total_average_viewers = 0
    for stream in data:
        try:
            average_viewers = float(stream[3])
            total_average_viewers += average_viewers
        except Exception:
            print("Probleme lors de la conversion en Float !", str(Exception), str(traceback.print_exc()))
    return total_average_viewers

def unique_viewers_total(data):
    total_unique_viewers = 0
    print(data[0])
    for stream in data:
        try:
            minutes_streamed = float(stream[13])
            print(type(minutes_streamed))
            if minutes_streamed != 0:
                unique_viewers = int(stream[14])
                total_unique_viewers += unique_viewers
        except Exception:
            print("Probleme lors de la conversion en Integer !", str(Exception), str(traceback.print_exc()))
    return total_unique_viewers

def display_data(data):
    month_data = []
    for i, stream in enumerate(data):
        streams = real_streams(stream)
        # nombre de stream durant le mois
        total_streams_month = len(streams)
        # nombre total de viewers moyen sur le mois
        total_average_viewers_month = average_viewers_total(streams)
        # viewers moyen sur le mois
        average_viewers_month = total_average_viewers_month / total_streams_month
        # nombre total de viewers unique sur le mois
        total_unique_viewers_month = unique_viewers_total(streams)
        month_data.extend([str(i +1) + " mois ", str(average_viewers_month) + ", Viewers moyen, et " + str(total_unique_viewers_month) + ", Viewers unique pour " + str(total_streams_month) + ", Streams "])
    return month_data



# enregistrement de mes data dans différentes variables
data_first_month = open_file("1er mois.csv")
data_second_month = open_file("2eme mois.csv")
data_third_month = open_file("3eme mois ( jusquau premier live tech.csv")
data_first_tech_month = open_file("1er mois tech.csv")
data_second_tech_month = open_file("2eme mois tech.csv")

data_all_month = [data_first_month, data_second_month, data_third_month, data_first_tech_month, data_second_tech_month]

info_data = open("1er mois.csv", "r")
info_data = csv.reader(info_data)
info = list(info_data)
infos = info[0]

for i, info in enumerate(infos):
    print(i, info)
#
#
# # traitements pour le premier mois de stream
#
# # nettoyage des datas
# first_month_streams = real_streams(data_first_month)
# # nombre de stream durant le mois
# total_streams_first_month = len(first_month_streams)
# # nombre total de viewers moyen sur le mois
# total_average_viewers_first_month = average_viewers_total(first_month_streams)
# # viewers moyen sur le mois
# average_viewers_first_month = total_average_viewers_first_month / total_streams_first_month
# # nombre total de viewers unique sur le mois
# total_unique_viewers_first_month = unique_viewers_total(first_month_streams)
#
# # traitements pour le second mois de stream
#
# # nettoyage des datas
# second_month_streams = real_streams(data_second_month)
# # nombre de stream durant le mois
# total_streams_second_month = len(second_month_streams)
# # nombre total de viewers moyen sur le mois
# total_average_viewers_second_month = average_viewers_total(second_month_streams)
# # viewers moyen sur le mois
# average_viewers_second_month = total_average_viewers_second_month / total_streams_second_month
# # nombre total de viewers unique sur le mois
# total_unique_viewers_second_month = unique_viewers_total(second_month_streams)
#
# # traitements pour le troisieme mois de stream
#
# # nettoyage des datas
# third_month_streams = real_streams(data_third_month)
# # nombre de stream durant le mois
# total_streams_third_month = len(third_month_streams)
# # nombre total de viewers moyen sur le mois
# total_average_viewers_third_month = average_viewers_total(first_month_streams)
# # viewers moyen sur le mois
# average_viewers_third_month = total_average_viewers_third_month / total_streams_third_month
# # nombre total de viewers unique sur le mois
# total_unique_viewers_third_month = unique_viewers_total(third_month_streams)
#
# # traitements pour le premier mois de stream tech
#
# # nettoyage des datas
# first_month_tech_streams = real_streams(data_first_tech_month)
# # nombre de stream durant le mois
# total_streams_first_tech_month = len(first_month_tech_streams)
# # nombre total de viewers moyen sur le mois
# total_average_viewers_first_tech_month = average_viewers_total(first_month_streams)
# # viewers moyen sur le mois
# average_viewers_first_tech_month  = total_average_viewers_first_tech_month / total_streams_first_tech_month
# # nombre total de viewers unique sur le mois
# total_unique_viewers_first_tech_month = unique_viewers_total(first_month_tech_streams)
#
# # traitements pour le second mois de stream tech
#
# # nettoyage des datas
# second_month_tech_streams = real_streams(data_second_tech_month)
# # nombre de stream durant le mois
# total_streams_second_tech_month = len(second_month_tech_streams)
# # nombre total de viewers moyen sur le mois
# total_average_viewers_second_tech_month = average_viewers_total(first_month_streams)
# # viewers moyen sur le mois
# average_viewers_second_tech_month = total_average_viewers_second_tech_month / total_streams_second_tech_month
# # nombre total de viewers unique sur le mois
# total_unique_viewers_second_tech_month = unique_viewers_total(second_month_tech_streams)
#
# print(str(total_streams_first_month) + " Streams", str(total_streams_second_month) + " Streams", str(total_streams_third_month) + " Streams", str(total_streams_first_tech_month) + " Streams", str(total_streams_second_tech_month) + " Streams")
# print(infos)
# print("-"*50)
# print(str(average_viewers_first_month) + " Viewers moyen sur le 1er mois de stream")
# print(str(total_unique_viewers_first_month) + " viewers unique sur")
# print("-"*50)
# print(str(average_viewers_second_month) + " Viewers moyen sur le 2eme mois de stream")
# print(str(total_unique_viewers_second_month) + " viewers unique sur")
# print("-"*50)
# print(str(average_viewers_third_month) + " Viewers moyen sur le 3eme mois de stream")
# print(str(total_unique_viewers_third_month) + " viewers unique sur")
# print("-"*50)
# print(str(average_viewers_first_tech_month) + " Viewers moyen sur le 1er mois de stream Tech")
# print(str(total_unique_viewers_first_tech_month) + " viewers unique sur")
# print("-"*50)
# print(str(average_viewers_second_tech_month) + " Viewers moyen sur le 2eme mois de stream Tech")
# print(str(total_unique_viewers_second_tech_month) + " viewers unique sur")
# print("-"*50)
#
#

# print(len(real_streams(data_first_month)))
# print(average_viewers_total(data_first_month))
# print(average_viewers_total(data_first_month) / len(real_streams(data_first_month)))
# print(len(real_streams(data_second_month)))
# print(average_viewers_total(data_second_month))
# print(average_viewers_total(data_second_month) / len(real_streams(data_second_month)))
# print(len(real_streams(data_third_month)))
# print(average_viewers_total(data_third_month))
# print(average_viewers_total(data_third_month) / len(real_streams(data_third_month)))
# print(len(real_streams(data_first_tech_month)))
# print(average_viewers_total(data_first_tech_month))
# print(average_viewers_total(data_first_tech_month) / len(real_streams(data_first_tech_month)))
# print(len(real_streams(data_second_tech_month)))
# print(average_viewers_total(data_second_tech_month))
# print(average_viewers_total(data_second_tech_month) / len(real_streams(data_second_tech_month)))


# print(len(real_streams(data_first_month)))
# print(average_viewers_total(data_first_month))
# print(average_viewers_total(data_first_month) / len(real_streams(data_first_month)))
# print("-"*500)
#
display_data = display_data(data_all_month)

for month in display_data:
    print(month)
