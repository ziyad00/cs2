from typing import Match
from django.db import models
from django.urls import reverse

class kfupm_tournament(models.Model):
    tr_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
     
    def get_absolute_url(self):
        return reverse('tour:teams', args=[self.id])

class kfupm_venue(models.Model):
    venue_name = models.CharField(max_length=255)
    venue_status = models.BooleanField(default=True)
    aud_capacity = models.IntegerField()

class kfupm_team(models.Model):
    tr_id = models.ForeignKey(kfupm_tournament, on_delete=models.CASCADE, related_name='teams')
    team_group = models.CharField(max_length=255)
    match_played = models.IntegerField()
    won = models.IntegerField()
    lose = models.IntegerField()
    draw = models.IntegerField()
    goal_for = models.IntegerField()
    goal_against = models.IntegerField()
    goal_diff = models.IntegerField()
    points = models.IntegerField()
    group_position = models.IntegerField()


class playing_position(models.Model):
    position_desc = models.CharField(max_length=255)


class player(models.Model):
    team_id = models.ForeignKey(kfupm_team, on_delete=models.CASCADE, related_name='teams')
    jersey_no = models.IntegerField()
    player_name = models.CharField(max_length=255)
    position_to_play  = models.ForeignKey(playing_position, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    
    def __str__(self) -> str:
        return self.player_name


class coach(models.Model):
    coach_name = models.CharField(max_length=255)


class referee(models.Model):
    referee_name = models.CharField(max_length=255)


class assistant_referee(models.Model):
    name = models.CharField(max_length=255)


class match_played(models.Model):
    play_stage = models.CharField(max_length=1)
    play_date = models.DateField()
    results = models.CharField(max_length=255)
    decided_by = models.CharField(max_length=255)
    goal_score = models.CharField(max_length=255)
    venue_id  = models.ForeignKey(kfupm_venue, on_delete=models.CASCADE)
    referee_id  = models.ForeignKey(referee, on_delete=models.CASCADE)
    audience = models.IntegerField()
    player_of_match  = models.ForeignKey(player, on_delete=models.CASCADE)
    stop1_sec = models.IntegerField() 
    stop2_sec = models.IntegerField() 


class match_details(models.Model):
    match_no   = models.ForeignKey(match_played, on_delete=models.CASCADE)
    team_id =  models.ForeignKey(kfupm_team, on_delete=models.CASCADE)
    play_stage = models.CharField(max_length=1)
    win_lose = models.CharField(max_length=1)
    decided_by = models.CharField(max_length=255)
    goal_score = models.IntegerField()
    penalty_score = models.IntegerField()
    asst_ref  =  models.ForeignKey(assistant_referee, on_delete=models.CASCADE)
    player_gk =  models.ForeignKey(player, on_delete=models.CASCADE)


class goal_details(models.Model):
    match_no   = models.ForeignKey(match_played, on_delete=models.CASCADE)
    player   = models.ForeignKey(player, on_delete=models.CASCADE,related_name='goals')
    team_id = models.ForeignKey(kfupm_team, on_delete=models.CASCADE)
    goal_time = models.DateTimeField()
    goal_type = models.CharField(max_length=255)
    play_stage = models.CharField(max_length=1)
    goal_schedule = models.CharField(max_length=255)
    goal_half = models.BooleanField()


class penalty_shootout(models.Model):
    match_no   = models.ForeignKey(match_played, on_delete=models.CASCADE)
    player   = models.ForeignKey(player, on_delete=models.CASCADE)
    team_id = models.ForeignKey(kfupm_team, on_delete=models.CASCADE)
    score_goal = models.CharField(max_length=1)
    kick_no = models.IntegerField()


class player_booked(models.Model):
    match_no   = models.ForeignKey(match_played, on_delete=models.CASCADE)
    player   = models.ForeignKey(player, on_delete=models.CASCADE, related_name='cards')
    team_id = models.ForeignKey(kfupm_team, on_delete=models.CASCADE)
    booking_time = models.DateTimeField()
    play_schedule = models.CharField(max_length=255)
    player_half = models.BooleanField()
    sent_off = models.CharField(max_length=1)

class player_in_out(models.Model):
    match_no   = models.ForeignKey(match_played, on_delete=models.CASCADE)
    player   = models.ForeignKey(player, on_delete=models.CASCADE)
    team_id = models.ForeignKey(kfupm_team, on_delete=models.CASCADE)
    in_out = models.CharField(max_length=255)
    time_in_out = models.DateTimeField()
    play_schedule = models.CharField(max_length=255)
    player_half = models.BooleanField()


class match_captain(models.Model):
    match_no   = models.ForeignKey(match_played, on_delete=models.CASCADE)
    team_id = models.ForeignKey(kfupm_team, on_delete=models.CASCADE)
    player_captain = models.ForeignKey(player, on_delete=models.CASCADE)


class team_coaches(models.Model):
    team_id = models.ForeignKey(kfupm_team, on_delete=models.CASCADE)
    tr_id = models.ForeignKey(kfupm_tournament, on_delete=models.CASCADE)
    coach_id = models.ForeignKey(coach, on_delete=models.CASCADE)

class penalty_gk(models.Model):
    match_no   = models.ForeignKey(match_played, on_delete=models.CASCADE)
    team_id = models.ForeignKey(kfupm_team, on_delete=models.CASCADE)
    player_gk =  models.ForeignKey(player, on_delete=models.CASCADE)


#class cards(models.Model):
#    player   = models.ForeignKey(player, on_delete=models.CASCADE, related_name='cards')
#    card = models.CharField(max_length=20)




     








