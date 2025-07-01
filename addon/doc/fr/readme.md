# Scanvox pour NVDA

* Auteur : Nael Sayegh
* URL : [infos@nael-accessvision.com](mailto:infos@nael-accessvision.com)
* Téléchargez la [version stable][1];
* Compatibilité avec NVDA : 2021.3 et plus récente;
* [Code source sur GitHub][2];

# Présentation

Cette extension utilise le logiciel Scanvox pour lire vos documents papier. Elle a été créée avec l'aide du développeur du logiciel et ne nécessite aucune installation supplémentaire.

## Prérequis

Pour utiliser cette extension vous devez avoir un scaner USB connecté à votre ordinateur compatible TWAIN ou WIA ce qui est le cas de la plupart des scanners.

## Comment ça marche

Pour utiliser cette extension, allez dans le menu de NVDA, puis sélectionnez Scanvox. Dans cette boîte de dialogue, vous pouvez démarrer un scan en cliquant sur le bouton Numériser. Le scan prend quelques secondes pour démarrer, puis, à la fin de la numérisation, le texte scané est automatiquement lu. Vous pouvez désactivez la lecture automatique en allant dans les paramètres de NVDA puis dans la catégorie Scanvox pour NVDA. Appuyez sur ce bouton jusqu'à ce que toutes les pages soient scannées. Si vous souhaitez supprimer la page que vous venez de scanner, vous pouvez appuyer sur le bouton "supprimer la dernière page numérisée" à côté du bouton scanner avec la touche tabulation ou en utilisant le raccourci alt+d. Une fois terminé, vous pouvez faire maj+tab à partir du bouton numérisé ou alt+t pour accéder à une zone d'édition qui contient le contenu de toutes les pages scanées. Dans cette zone d'édition, si vous souhaitez passer rapidement d'une page à l'autre, vous pouvez utiliser les boutons page précédente et page suivante, ou utiliser les raccourcis ctrl+shift+flèche haut et ctrl+shift+flèche bas. Vous pouvez enregistrer le fichier avec le bouton correspondant.
Si vous souhaitez supprimer les pages scannées pour scanner un nouveau document, vous pouvez appuyer sur le bouton pour annuler toutes les pages numérisées.
Lorsque vous quittez Scanvox, toutes les pages scannées sont effacées.

### Raccourcis clavier

L'extension "Scanvox pour NVDA" peut être lancée de n'importe où sur votre ordinateur en appuyant sur nvda+alt+s. Ce geste peut être modifié dans la boîte de dialogue des gestes d'entrée.

## Changements

### Version 2025.07.01

  * Compatibilité testée avec NVDA 2025.1

### Version 2024.08.15

  * Dans la zone d'édition, vous pouvez désormais utiliser les touches de page précédente et suivante ou ctrl+shift+flèche haut et ctrl+shift+flèche bas pour passer rapidement d'une page à l'autre
  * Ajout d'un bouton pour supprimer la dernière page scannée
  * Inversion des formats de fichiers dans la liste des formats de la boîte de dialogue d'enregistrement de fichier. Le format par défaut est docx.
  * Modernisation du système de mise à jour pour utiliser l'API GitHub pour vérifier et installer les nouvelles versions. Cela corrige également le problème d'installation des versions de développement.
  * Correction du problème de chargement du module qui se bloquait lorsqu'aucune connexion internet n'était détectée.

### Version 2024.07.02

  * Correction d'un problème où le numéro de page continuait à augmenter après avoir cliquer sur supprimer

### Version 2024.06.01

  * Ajout d'un canal de mise à jour de développement pour les traducteurs et le test de nouvelles fonctionnalités
  * Ajout de la traduction turque
  * Lors de l'enregistrement d'un document Word, chaque page est ajoutée comme une nouvelle page dans le fichier.
  * Ajout d'un message dans le journal NVDA pour indiquer que Scanvox est chargé
  * Documentation mise à jour

### Version 2024.05.04

  * Amélioration du système de mise à jour
  * Mise à jour de la traduction russe
  * Correction de la traduction française
  * Correction d'un bug qui ne supprimait pas le contenu de la zone d'édition lors de l'appui sur le bouton de suppression
  * Placement automatique du curseur au début de la page scannée dans la zone d'édition.
  * Ajout du numéro de page en haut de chaque page scannée dans la zone d'édition
  * Déplacement du menu Scanvox du menu outils vers le menu principal

### Version 2024.03.20

  * Ajout de la traduction tchèque
  * Ajout de la traduction portugaise
  * Ajout d'une zone d'édition avant le bouton de numérisation permettant de lire immédiatement le texte qui vient d'être numérisé
  * Ajout d'un paramètre pour désactiver / activer la lecture automatique d'un document, rendez-vous dans le menu des paramètres de NVDA puis Scanvox pour NVDA
  * Ajout de la traduction russe

### Version 2024.01.10

  * Modification du système de mise à jour pour ajouter un bouton "Quoi de neuf" qui ouvre l'aide avec les nouveauté de la version
  * Ajout de la lecture automatique de la page scanée après la numérisation
  * Ajout d'un séparateur de pagedans les fichier (20 astérisques) pour permettre de savoir quand on change de page

### Version 2024.01.03

  * Mise à jour de l'aide en français

### Version 2023.12.29
  * Première version

Copyright ©: 2024 (Nael Sayegh et Nael-Accessvision

<!-- links section -->

[1]: https://github.com/Nael-Sayegh/scanvox-for-nvda/releases/download/2025.07.01/scanvox-2025.07.01.nvda-addon

[2]: https://github.com/Nael-Sayegh/scanvox-for-nvda
