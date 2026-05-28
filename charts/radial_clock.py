import plotly.graph_objects as go


USER_COLORS = {
    "Ashanti": "#4f6dff",
    "Gabi": "#FF8FD8",
    "Maribel": "#FF8A3D"
}


def hex_to_rgb(hex_color):

    hex_color = hex_color.lstrip("#")

    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def get_dominant_span(hours, dominant_users, user):

    if not hours or not dominant_users or user is None:
        return None, None

    matching_hours = [
        hour
        for hour, dominant_user in zip(hours, dominant_users)
        if dominant_user == user
    ]

    if not matching_hours:
        return None, None

    runs = []
    current_run = [matching_hours[0]]

    for hour in matching_hours[1:]:
        previous_hour = current_run[-1]
        if hour == previous_hour + 1:
            current_run.append(hour)
        else:
            runs.append(current_run)
            current_run = [hour]

    runs.append(current_run)

    if len(runs) > 1 and runs[0][0] == 0 and runs[-1][-1] == 23:
        runs = [runs[-1] + runs[0], *runs[1:-1]]

    longest_run = max(runs, key=len)

    start_hour = longest_run[0]
    end_hour = (longest_run[-1] + 1) % 24

    return start_hour, end_hour


def create_clock_chart(data, mood_map=None):

    fig = go.Figure()

    # ---------------------------------
    # COLORS
    # ---------------------------------

    colors = []
    border_colors = []
    dominant_moods = []

    for hour_index, user in enumerate(data["dominant_users"]):

        if user is None:

            colors.append("rgba(255,255,255,0.18)")
            border_colors.append("rgba(255,255,255,0.18)")
            dominant_moods.append("Dark")

        else:

            r, g, b = hex_to_rgb(USER_COLORS[user])
            rgba = f"rgba({r},{g},{b},0.78)"

            colors.append(rgba)
            border_colors.append(rgba)

            if mood_map and user in mood_map and hour_index < len(mood_map[user]):
                dominant_moods.append(mood_map[user][hour_index])
            else:
                dominant_moods.append("Dark")

    # ---------------------------------
    # CLOCK RING
    # ---------------------------------

    line_widths = [1] * len(data["hours"]) if "hours" in data else [1] * 24

    fig.add_trace(
        go.Barpolar(
            r=[0.30] * 24,
            base=[0.50] * 24,
            theta=[h * 15 for h in data["hours"]],
            width=[13] * 24,
            marker_color=colors,
            marker_line_color=border_colors,
            marker_line_width=line_widths,
            opacity=1.0,
            customdata=list(
                zip(
                    data["dominant_users"],
                    data["hours"],
                    dominant_moods
                )
            ),
            hovertemplate=(
                "User: %{customdata[0]}<br>"
                "Hour: %{customdata[1]}:00<br>"
                "Mood: %{customdata[2]}<br>"
                "<extra></extra>"
            )
        )
    )

    # ---------------------------------
    # CENTER TEXT
    # ---------------------------------

    center_user = "Ashanti"
    center_item = None

    for item in data.get("listening_share", []):
        if item.get("user") == center_user:
            center_item = item
            break

    peak_user = center_user if center_item else data.get("peak_user")
    color_for_text = USER_COLORS.get(center_user, "#ffffff")

    dominant_start_hour, dominant_end_hour = get_dominant_span(
        data.get("hours", []),
        data.get("dominant_users", []),
        center_user
    )

    if dominant_start_hour is not None:
        time_text = f"{dominant_start_hour}:00 - {dominant_end_hour}:00"
    else:
        peak_hour = data.get("peak_hour")
        end_hour = (peak_hour + 1) % 24 if peak_hour is not None else data.get("end_hour")
        time_text = f"{peak_hour}:00 - {end_hour}:00"

    text = (
        "<span style='font-size:12px;color:rgba(255,255,255,0.65)'>Dominant time</span><br><br>"
        f"<span style='font-size:28px;color:{color_for_text};font-weight:700'>{time_text}</span><br><br>"
        f"<span style='font-size:20px;color:{color_for_text};font-weight:700'>{peak_user}</span>"
    )

    fig.add_annotation(
        x=0.5,
        y=0.5,
        text=text,
        showarrow=False,
        font=dict(size=14, color="white")
    )

    # ---------------------------------
    # LAYOUT
    # ---------------------------------

    fig.update_layout(
        polar=dict(
            bgcolor="rgba(0,0,0,0)",
            radialaxis=dict(
                visible=False,
                range=[0, 0.96],
                showgrid=False,
                ticks=""
            ),
            angularaxis=dict(
                tickmode="array",
                tickvals=[0, 45, 90, 135, 180, 225, 270, 315],
                ticktext=["0", "3", "6", "9", "12", "15", "18", "21"],
                tickfont=dict(size=9, color="white"),
                ticklabelstep=1,
                color="white",
                direction="clockwise",
                showline=False,
                showgrid=False,
                ticks="",
                rotation=90
            )
        ),
        showlegend=False,
        height=260,
        width=260,
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    return fig