Module Compofig - Documentation

1. Objectif
Le module Compofig vise à modéliser la conceptualisation des composants d'un ordinateur et leurs règles de compatibilité. Il sert de base pour :

Définir les types de composants et leurs attributs
Établir les règles de compatibilité
Permettre la validation d'une configuration

2. Composants et Spécificités
2.1 Processeur (CPU)

Socket (AM4, AM5, LGA1200, LGA1700)
TDP (W)
Nombre de cœurs
Nombre de threads
Fréquence de base (GHz)
Fréquence boost (GHz)
Graphique intégré (oui/non)
Cache (Mo)
Support RAM (DDR4/DDR5)
PCIe Version supportée

2.2 Carte Mère (Motherboard)

Socket (AM4, AM5, LGA1700)
Format (ATX, micro-ATX, mini-ITX)
Type RAM (DDR4, DDR5)
Nombre slots RAM
Génération PCIe
Slots M.2
Ports SATA
Format USB en façade supporté
TDP CPU supporté (W)

2.3 RAM

Capacité (GB)
Type (DDR4, DDR5)
Fréquence (MHz)
Latence (CL)
Voltage
Format (DIMM/SO-DIMM)

2.4 Stockage

Type (SSD/HDD)
Capacité (GB/TB)
Interface (SATA/NVMe)
Format (2.5", 3.5", M.2)
Vitesse lecture/écriture (MB/s)
TBW pour SSD

2.5 Alimentation (PSU)

Puissance (W)
Format (ATX, SFX)
Certification (80+ White/Bronze/Gold/Platinum)
Modularité (Non/Semi/Full)
Longueur (mm)
Rails 12V

2.6 Boîtier (Case)

Format supporté (ATX, micro-ATX, mini-ITX)
Longueur GPU max (mm)
Hauteur CPU Cooler max (mm)
Longueur PSU max (mm)
Ventilateurs inclus
Emplacements ventilateurs
Ports en façade
Format d'alimentation supporté

2.7 GPU (optionnel)

Mémoire vidéo (GB)
Type mémoire (GDDR6/6X)
TDP (W)
Longueur (mm)
Connecteur alimentation requis
PCIe Version
Sorties vidéo

2.8 Ventirad CPU (optionnel)

Hauteur (mm)
TDP supporté (W)
Compatibilité socket
Ventilateur inclus
Niveau sonore (dB)

3. Règles de Compatibilité
3.1 Règles Basiques

Le socket du CPU doit correspondre au socket de la carte mère
La puissance du PSU doit être supérieure à la somme des TDP des composants
Le format de la carte mère doit être supporté par le boîtier
Le format de l'alimentation doit être supporté par le boîtier

3.2 Règles de Mémoire

Le type de RAM doit être supporté par le CPU et la carte mère
Le nombre de barrettes ne doit pas dépasser le nombre de slots
La fréquence de la RAM doit être supportée par le CPU et la carte mère
Les barrettes doivent être installées par paires pour le dual channel

3.3 Règles Dimensionnelles

La longueur du GPU doit être inférieure à l'espace disponible dans le boîtier
La hauteur du ventirad doit être inférieure à l'espace disponible dans le boîtier
La longueur de l'alimentation doit être inférieure à l'espace disponible dans le boîtier

3.4 Règles de Puissance

L'alimentation doit fournir suffisamment de connecteurs PCIe pour le GPU
Le ventirad doit supporter le TDP du CPU
Le système de refroidissement de la carte mère doit supporter le TDP du CPU
Prévoir une marge de 20% minimum sur la puissance de l'alimentation

3.5 Règles Spécifiques

Vérifier la compatibilité des profils mémoire XMP/DOCP
La génération PCIe doit être compatible entre GPU, CPU et carte mère
Les ventilateurs doivent avoir la bonne taille pour les emplacements du boîtier
Les ports USB en façade du boîtier doivent être supportés par la carte mère
Vérifier la compatibilité du format M.2 (Key M, Key B, etc.)
Le ventirad ne doit pas interférer avec les slots RAM
En cas de GPU vertical, vérifier la compatibilité du riser PCIe

3.6 Règles de Performance

RAM en dual channel recommandée
SSD NVMe recommandé pour le système
PSU Gold ou mieux recommandé pour l'efficacité
Ventilation positive recommandée (plus d'entrée que de sortie d'air)

3.7 Règles Avancées

Vérifier la liste de compatibilité RAM (QVL) de la carte mère
Considérer la largeur du GPU pour les slots PCIe adjacents
Vérifier la compatibilité BIOS pour les nouvelles générations de CPU
Considérer les besoins en refroidissement selon le cas d'usage
Vérifier la compatibilité des technologies (ResizableBAR, SAM, etc.)
