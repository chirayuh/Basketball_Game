import pgzrun

WIDTH = 800
HEIGHT = 600

show_popup = False
popup_text_lines = [
    "🎉 You unlocked a reward! 🎁",
    "Click anywhere to continue."
]

def draw():
    screen.clear()
    screen.fill((30, 30, 60))
    screen.draw.text("Press SPACE to show popup", center=(WIDTH//2, 100), fontsize=40, color="white")

    if show_popup:
        # Dark background overlay
        screen.draw.filled_rect(Rect((0, 0), (WIDTH, HEIGHT)), (0, 0, 0, 120))
        
        # Popup box
        popup_rect = Rect((200, 200), (400, 200))
        screen.draw.filled_rect(popup_rect, (50, 50, 50))
        screen.draw.rect(popup_rect, "white")

        # Draw lines of text manually
        for i, line in enumerate(popup_text_lines):
            screen.draw.text(
                line,
                center=(WIDTH//2, 240 + i * 40),
                fontsize=30,
                color="white"
            )

def on_key_down(key):
    global show_popup
    if key == keys.SPACE:
        show_popup = True

def on_mouse_down(pos):
    global show_popup
    if show_popup:
        show_popup = False

pgzrun.go()
