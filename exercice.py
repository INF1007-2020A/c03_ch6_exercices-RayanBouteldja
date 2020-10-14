#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> bool:
        # TODO: Demander les valeurs ici
    list=[]
    while len(list)<10:
        values=list.append(int(input('écrivez 10 nombres entiers: ')))
    ordonne=True
    for index in range(len(list)-1):
        if list[index]>list[index+1]:
            ordonne=False
            print('Ce n\'est pas ordonné')
            break
    if ordonne:
       print('La liste est ordonné')
    return None


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: Demander les mots ici
        pass
    mot1=list(input('mot 1: '))
    mot2=list(input('mot 2: '))
    if len(mot1)==len(mot2):
        for letter in mot1:
            if letter in mot2:
               mot2.remove(letter)
        if len(mot2)==0:
            print('annagramme')
        else:
            print('pas annagramme')
    else:
        print('pas annagramme')

    return None


def contains_doubles(items: list) -> bool:
    if len(items)==len(set(items)):
        res='pas de doublons'
    else:
        res='contient des doublons'
    
    return res


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    moyenne=[]
    for name in student_grades:
       somme_note=0
       for note in student_grades[name]:
           somme_note+=note
       student_grades[name]=somme_note/len(student_grades[name])
    moyenne.append(student_grades[name])
    moyenne=sorted(moyenne,reverse=True)
    for name in student_grades:
        if student_grades[name]==moyenne[0]:
           return {name:student_grades[name]}


def histogram(sentence: str) -> tuple:
    # TODO: Créer l'histogramme a l'aide d'un dictionnaire
    histogramme={}
    sentence_2=set(sentence)
    for lettre in sentence_2:
        histogramme[lettre]=sentence.count(lettre)

    #       Afficher l'histogramme et les lettres les plus fréquentes
    #       Retourner l'histogramme et le tableau de lettres

    return {}, []


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingrédients et enregistrer dans une structure de données 
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    name, result = best_grades(grades)
    print(f"{name} a la meilleure moyenne: {result}")
    
    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
