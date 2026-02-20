from typing import List, Tuple
from abc import ABC, abstractmethod
from mlx import Mlx
from srcs.mlx_tools.BaseMLX import MlxVar, MyMLX
from srcs.maze_visualizer.MazeParams import MazeParams


class MazeVisualizer(MyMLX, ABC):
    def __init__(self, w: int, h: int, entry: Tuple, exit: Tuple):
        super().__init__(w, h)
        self.const = MazeParams()
        self.entry = entry
        self.exit = exit

    @abstractmethod
    def display_maze(self, maze: List[List[int]]) -> None:
        pass


class MazeVisualizerOne(MazeVisualizer):
    def display_maze(self, maze: List[List[int]]) -> None:
        """
        Maze rule:
        0:N, 1:E, 2:S, 3:W
        0 -> open, 1 -> closed
            N
        W       E
            S
        """
        maze_w, maze_h = len(maze[0]), len(maze)
        spacing = self.const.grid_size
        wall = self.const.wall_thickness
        for y in range(maze_h):
            for x in range(maze_w):
                top_x = x * spacing
                top_y = y * spacing
                bottom_x = (x + 1) * spacing
                bottom_y = (y + 1) * spacing
                val = maze[x][y]
                print(f"x: {x}, y: {y}, {val}, "
                      f"{(val >> 3) & 1}{(val >> 2) & 1}{(val >> 1) & 1}{(val >> 0) & 1}")
                if (val >> 0) & 1:
                    top_y += wall
                if (val >> 3) & 1:
                    top_x += wall
                if (val >> 1) & 1:
                    bottom_y -= wall
                if (val >> 2) & 1:
                    bottom_x -= wall


       


def maze_tester():
    demo = [
        [15, 15, 15, 15],
        [15, 5, 10, 15],
        [15, 6, 8, 15],
        [15, 15, 15, 15]
    ]
    try:
        w, h = MazeParams.get_maze_size_in_pixels(len(demo[0]), len(demo))
        visualizer = MazeVisualizerOne(w, h, (0, 0), (3, 3))
        visualizer.set_background(visualizer.mlx.buff_img,
                                  (0, 0), visualizer.mlx.buff_img.w,
                                  visualizer.mlx.buff_img.w, 0xFF00FF00)
        visualizer.display_maze(demo)
        visualizer.put_buffer_image()
        visualizer.start_mlx()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    maze_tester()
