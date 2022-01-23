from textual.app import App
from textual.widgets import Placeholder


class GridTest(App):
    async def on_mount(self) -> None:
        """Make a simple grid arrangement."""

        grid = await self.view.dock_grid(edge="left", name="left")

        grid.add_column(fraction=1, name="left", min_size=20)
        grid.add_column(size=30, name="center")
        grid.add_column(fraction=1, name="right")

        grid.add_row(fraction=1, name="top", min_size=2)
        grid.add_row(fraction=2, name="middle")
        grid.add_row(fraction=1, name="bottom")

        grid.add_areas(
            area1="left,top",
            area2="center,middle",
            area3="left-start|right-end,bottom",
            area4="right,top-start|middle-end",
        )

        self.area1 = Placeholder(name="area1")
        self.area2 = Placeholder(name="area2")
        self.area3 = Placeholder(name="area3")
        self.area4 = Placeholder(name="area4")

        grid.place(
            area1=self.area1 ,
            area2=self.area2 ,
            area3=self.area3 ,
            area4=self.area4 ,
        )
    
    def on_key(self, event):
        if event.key.isdigit():
            self.background = f"on color({event.key})"
            self.area1.has_focus = False
            self.area2.has_focus = False
            self.area3.has_focus = False
            self.area4.has_focus = False
            if event.key == '1':
                self.area1.has_focus = True
            if event.key == '2':
                self.area2.has_focus = True
            if event.key == '3':
                self.area3.has_focus = True
            if event.key == '4':
                self.area4.has_focus = True
                


GridTest.run(title="Grid Test", log="textual.log")
