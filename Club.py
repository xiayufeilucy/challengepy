class Club(object):
    def __init__(self, club_name, club_description):
        self.club_name = club_name
        self.club_tags = []
        self.club_description = club_description
        self.fav_count = []

    def add_club_tag(self, club_tag):
        self.club_tags.append(club_tag)

    def jsonify(self):
        return {"club_name": self.club_name, "club_tags": self.club_tags, "club_description": self.club_description, "club_like": len(self.fav_count)}

    def like(self, user):
        if (user not in self.fav_count):
            self.fav_count = self.fav_count.append(user)