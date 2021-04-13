from re import match
from django.contrib import admin
from .models import kfupm_tournament,kfupm_team,kfupm_venue,player,player_booked,penalty_gk,penalty_shootout,player_in_out,playing_position,match_played,referee,assistant_referee,team_coaches,goal_details,match_details,coach,match_captain

admin.site.register(kfupm_tournament)
admin.site.register(kfupm_team)
admin.site.register(kfupm_venue)
admin.site.register(player)
admin.site.register(player_booked)
admin.site.register(penalty_gk)
admin.site.register(penalty_shootout)
admin.site.register(player_in_out)
admin.site.register(playing_position)
admin.site.register(match_played)
admin.site.register(referee)
admin.site.register(assistant_referee)
admin.site.register(team_coaches)
admin.site.register(goal_details)
admin.site.register(coach)
admin.site.register(match_details)
admin.site.register(match_captain)

'''

'''

# Register your models here.
