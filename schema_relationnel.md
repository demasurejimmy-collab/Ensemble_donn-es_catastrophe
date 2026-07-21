schéma mermaid 
```mermaid
erDiagram
    PAYS ||--o{ EVENEMENTS : "1 à N"
    TYPE_CATASTROPHE ||--o{ EVENEMENTS : "1 à N"

    PAYS {
        int id_pays PK
        string nom_pays
        string continent
    }

    EVENEMENTS {
        int id_event PK
        date date_event
        float intensite
        float pertes_economiques
        int delai_intervention
        int id_pays FK
        int id_type FK
    }

    TYPE_CATASTROPHE {
        int id_type PK
        string libelle_type
    }
