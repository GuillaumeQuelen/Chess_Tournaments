from views.menu_view import MenuView
from controllers.player_controller import PlayerController
from controllers.tournaments_controller import TournamentsController
from controllers.report_controller import ReportController
from views.report_view import ReportView


class AppController:
    def __init__(self):
        self.menu = MenuView()
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentsController()
        self.report_controller = ReportController()
        self.report_view = ReportView()

    def run(self):
        while True:
            choix = self.menu.show_menu()
            if choix == "1":
                self.player_controller.create_player()
            elif choix == "2":
                self.tournament_controller.run()
            elif choix == "3":
                while True:
                    choix_r = self.report_view.show_menu()
                    if choix_r == "1":
                        self.report_controller.list_all_players()
                    elif choix_r == "2":
                        self.report_controller.list_all_tournaments()
                    elif choix_r == "3":
                        self.report_controller.tournament_details()
                    elif choix_r == "4":
                        self.report_controller.list_tournament_players()
                    elif choix_r == "5":
                        self.report_controller.list_tournament_rounds()
                    elif choix_r == "6":
                        break
            elif choix == "4":
                print("Au revoir !")
                break