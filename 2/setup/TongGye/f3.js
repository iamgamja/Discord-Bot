module.exports = async (client) => {
  client._.TongGye.f3 = async () => {
    try {
  
      const line_chart = ChartJSImage().chart({
        "type": "line",
        "data": {
          "labels": [...Array(24).keys()],
          "datasets": [
            {
              "label": "메시지 수",
              "borderColor": "rgb(255,+99,+132)",
              "backgroundColor": "rgba(255,+99,+132,+.5)",
              "data": ( await client.db.get() ).TongGye.B
            }
          ]
        },
        "options": {
          "scales": {
            "yAxes": [
              {
                "stacked": true,
              }
            ]
          }
        }
      })
      .backgroundColor('white')
      .width(500)
      .height(300);
  
      return await line_chart.toBuffer();
  
    } catch(e) { await client.Error(e) }
  }
}