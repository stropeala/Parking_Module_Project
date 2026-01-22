from clients_draft import clients_draft
from db_draft import db_end_draft

if __name__ == "__main__":
    ids = []

    ids.append(
        clients_draft(
            "drafts/data/clients_draft.json",
            "Frank",
            "Fleming",
            "(810) 011-4394",
            "Port Huron, MI",
        )
    )
    ids.append(
        clients_draft(
            "drafts/data/clients_draft.json",
            "Keith",
            "Wood",
            "(475) 651-6147",
            "Bridgeport, CT",
        )
    )

    for id in ids:
        filepath = "drafts/data/clients_draft.json"
        db_end_draft(filepath, id)
