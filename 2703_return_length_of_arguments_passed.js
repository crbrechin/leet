/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    $i = 0
    args.forEach(() => {$i++} )
    return $i
};

/**
 * argumentsLength(1, 2, 3); // 3
 */
