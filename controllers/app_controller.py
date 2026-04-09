from views.menu_view import MenuView
from controllers.player_controller import PlayerController
from controllers.tournaments_controller import TournamentsController
from controllers.report_controller import ReportController


class AppController:
    def __init__(self):
        self.menu = MenuView()
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentsController()
        self.report_controller = ReportController()

    def run(self):
        while True:
            choix = self.menu.show_menu()
            if choix == "1":
                self.player_controller.run()
            elif choix == "2":
                self.tournament_controller.run()
            elif choix == "3":
                self.report_controller.run()
            elif choix == "4":
                print("Au revoir !")
                break
