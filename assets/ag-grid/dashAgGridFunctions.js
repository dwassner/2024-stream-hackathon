var dagfuncs = (window.dashAgGridFunctions = window.dashAgGridFunctions || {});

dagfuncs.percentFormat = function (params, fractionDigits) {
  return params.value.toLocaleString(undefined, {
    style: "percent",
    minimumFractionDigits: fractionDigits,
    maximumFractionDigits: fractionDigits,
  });
};

dagfuncs.currencyFormat = function (params, currency, fractionDigits) {
  let value = parseFloat(params.value.toFixed(2));
  if (!fractionDigits) return currency + value.toLocaleString();
  return (
    currency +
    value.toLocaleString(undefined, {
      minimumFractionDigits: fractionDigits,
      maximumFractionDigits: fractionDigits,
    })
  );
};
