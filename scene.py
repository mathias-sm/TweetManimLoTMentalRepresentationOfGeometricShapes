from manim import *

config.max_files_cached = 500


class Tweet(Scene):
    def construct(self):
        # Load images and prepare some colors/positions
        # NOTE : blombos.jpg should be acquired somewhere, e.g. at the following
        # adresse https://www.cnrs.fr/fr/decouverte-du-plus-ancien-dessin-au-crayon
        blombos = ImageMobject("./blombos.jpg").scale(0.75)
        credit = Text("©D'Errico/Henshilwood/Nature", font_size=11).move_to(
            5 * LEFT + 2 * UP
        )
        head = SVGMobject("brain.svg").scale(2)

        zigzag = SVGMobject("zigzag.svg", unpack_groups=False).scale(0.75)
        zigzag.move_to(5 * RIGHT + 2 * UP)
        for x in zigzag:
            x.set_style(stroke_width=14)

        pr1 = (
            SVGMobject("program.svg", unpack_groups=False)
            .next_to(zigzag, 2 * DOWN)
            .scale(1.25)
        )
        for x in pr1:
            x.set_style(stroke_width=3.3, stroke_color="#FFFFFF")
        pr1[-1].set_style(stroke_color="#007e6f")
        pr1[-2].set_style(stroke_color="#007e6f")
        pr1[-1][-1].set_style(stroke_width=12, stroke_color="#007e6f")
        pr1[-2][-1].set_style(stroke_width=12, stroke_color="#007e6f")

        parallel = (
            SVGMobject("parallel.svg", unpack_groups=False)
            .next_to(zigzag, 2 * DOWN)
            .scale(1.25)
        )
        for x in parallel:
            x.set_style(stroke_width=3.3, stroke_color="#FFFFFF")
        parallel[-3].set_style(stroke_color="#848da2")
        parallel[-2].set_style(stroke_width=12, stroke_color="#848da2")

        metapr = (
            SVGMobject("meta_program.svg", unpack_groups=False)
            .next_to(pr1, 1.5 * DOWN)
            .scale(0.75)
        )
        for x in metapr:
            x.set_style(stroke_width=3.3, stroke_color="#FFFFFF")
        metapr[-3].set_style(stroke_color="#007e6f")
        metapr[-2].set_style(stroke_color="#e88d00")
        metapr[-1].set_style(stroke_color="#848da2")

        head[0].set_style(
            fill_opacity=1, stroke_width=0, stroke_opacity=0, fill_color=GREY_D
        )
        head[1].set_style(stroke_width=12)

        # Show the zigzag, then scale it down and show the head + "brain"
        self.play(FadeIn(blombos))
        self.play(
            LaggedStart(
                blombos.animate.scale(0.25).move_to(5 * LEFT + 1 * UP),
                Write(credit),
                lag_ratio=0.5,
            ),
            run_time=1,
        )
        self.play(Write(head))

        # Copy the zigzag, move it to the head
        blombos_to_induce = blombos.copy()
        self.play(blombos_to_induce.animate.move_to(RIGHT * 0 + 1 * UP))

        # Replace it with a "code" example suggesting that geometric shapes are
        # programs
        code_idea = Code(
            code="# mental\n# representations\n# are programs",
            language="python",
            style="monokai",
            font_size=18,
            font="IBM Plex Mono",
            background="window",
        )
        code_idea.move_to(blombos_to_induce)
        code_idea.set_opacity(0.95)
        self.play(FadeOut(blombos_to_induce), FadeIn(code_idea))
        self.wait()

        # Now write the program for a first zigzag, show its output, and store
        # it as a cog symbol
        self.play(Write(pr1))
        self.play(Write(zigzag[0]))
        self.wait()
        pr1_1 = pr1.copy()
        self.play(ReplacementTransform(pr1_1, metapr[-3]))
        self.wait()

        # Now write the program for a second zigzag, show its output, and store
        # it as a cog symbol
        pr2 = pr1.copy()
        pr2[-1].set_style(stroke_width=3.3, stroke_color="#e88d00")
        pr2[-2].set_style(stroke_width=3.3, stroke_color="#e88d00")
        pr2[-1][-1].set_style(stroke_width=12, stroke_color="#e88d00")
        pr2[-2][-1].set_style(stroke_width=12, stroke_color="#e88d00")
        pr2[-1][-1].flip()
        pr2[-2][-1].flip()
        self.play(ReplacementTransform(pr1, pr2))
        self.play(Write(zigzag[1]))
        self.wait()
        pr2_2 = pr2.copy()
        self.play(ReplacementTransform(pr2_2, metapr[-2]))
        self.play(Write(metapr[-5]))
        self.wait()

        # Now write the program for the two parallel lines, show its output, and
        # store it as a cog symbol
        self.play(ReplacementTransform(pr2, parallel))
        self.play(Write(zigzag[2]))
        self.wait()
        pr3_2 = parallel.copy()
        self.play(ReplacementTransform(pr3_2, metapr[-1]))
        self.play(Write(metapr[-4]))
        self.wait()

        # Finally, unwrite the mess of programs and highlight the main point
        self.play(Unwrite(zigzag), Unwrite(parallel), run_time=1)
        self.play(metapr.animate.move_to(5 * RIGHT + UP))
        conclusion = Text(
            text="Geometric Shape Perception as Program Induction",
            font_size=36,
        )
        conclusion.next_to(head, DOWN)
        self.play(Write(conclusion), run_time=1)
        self.wait()
        self.wait()
