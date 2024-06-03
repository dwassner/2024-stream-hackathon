window.dash_clientside = Object.assign({}, window.dash_clientside, {
  placements: {
    prepare_chart: function (data, id) {
      if (!data) return window.dash_clientside.no_update;
      preparePlacementChart(data, id);
      return window.dash_clientside.no_update;
    },
  },
});

function preparePlacementChart(data, id) {
  const yaxes = [
    {
      title: { text: "Ad Spend" },
      gridLineWidth: 0,
      visible: false,
      labels: {
        formatter: function () {
          return "$" + this.value.toLocaleString();
        },
      },
    },
    {
      title: { text: "Ad Sales" },
      gridLineWidth: 0,
      labels: {
        formatter: function () {
          return "$" + this.value.toLocaleString();
        },
      },
    },
    {
      title: { text: "CPC" },
      gridLineWidth: 0,
      labels: {
        formatter: function () {
          return "$" + this.value.toFixed(2);
        },
      },
      opposite: true,
    },
    {
      title: { text: "CVR" },
      gridLineWidth: 0,
      labels: {
        formatter: function () {
          return this.value.toFixed(1) + "%";
        },
      },
      opposite: true,
    },
  ];
  const options = {
    chart: { type: "spline" },
    title: { text: null, align: "left" },
    tooltip: ToolTipFormatter(),
    legend: { labelFormatter: legendFormatter },
    xAxis: {
      categories: data.categories,
      crosshair: { width: 1, color: "black" },
      tickmarkPlacement: null,
    },
    yAxis: yaxes,
    plotOptions: {
      series: {
        marker: { enabled: false },
        events: {
          legendItemClick: function () {
            let isVisible = this.yAxis.visible;
            this.chart.yAxis[this.yAxis.index].update({ visible: !isVisible });
          },
        },
      },
      spline: { pointPlacement: "on" },
    },
    series: data.data,
    credits: { enabled: false },
  };
  Highcharts.setOptions({ lang: { thousandsSep: "," } });
  Highcharts.chart(id, options);
}

function ToolTipFormatter() {
  return {
    shared: true,
    hideDelay: 0,
    useHTML: true,
    headerFormat:
      "<table><tr><th></th><th>{point.key}</th><th></th></tr>" +
      "<tr><th>Stat</th><th>Placement</th><th>Value</th></tr>",
    pointFormat:
      "<tr><td>{series.userOptions.legendName}&nbsp;&nbsp;&nbsp;</td>" +
      '<td><span style="color:{point.color}">\u25CF </span>{series.name}</td>' +
      '<td style="text-align: right"><b>{point.y}</b></td></tr>',
    footerFormat: "</table>",
  };
}

function legendFormatter() {
  return this.userOptions.legendName;
}