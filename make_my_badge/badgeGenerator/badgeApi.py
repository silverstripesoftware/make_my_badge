from createBadges import BadgeImage


def make_badge(name,company,id):
    badge = BadgeImage("badge_template.png")
    badge.drawPerson(name)
    badge.drawCompany(company)
    badge.drawId(id)
    return badge