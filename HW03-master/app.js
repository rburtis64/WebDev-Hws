var main = function() {
  'use strict';
  var cardDeck = $('#cardDeck').playingCards();
  cardDeck.spread();
  var hand = [];
  var table = [];
  var reset = () => {
    cardDeck = $('#cardDeck').playingCards();
    cardDeck.spread();
    hand = [];
    table = [];
    showHand();
  };
  var showError = function(msg) {
    $('#error')
      .html(msg)
      .show();
    setTimeout(function() {
      $('#error').fadeOut('slow');
    }, 3000);
  };
  var showHand = function() {
    var el = $('#yourHand');
    el.html('');
    for (var i = 0; i < hand.length; i++) {
      el.append(hand[i].getHTML());
    }
  };
  var showTable = function(){
    var e1 = $('#table');
    e1.html('');
    for(var i = 0; i < table.length; i++){
      e1.append(table[i].getHTML());
    }
  };
  var doShuffle = function() {
    cardDeck.shuffle();
    cardDeck.spread();
  };
  var DrawCard = function() {
    var c = cardDeck.draw();
    if (!c) {
      showError('no more cards');
      return;
    }
    hand[hand.length] = c;
    cardDeck.spread();
    showHand();
  };
  var DrawHand = () => {
    while (hand.length < 2) {
      DrawCard();
    }
    var SetTable = () => {
      while (table.length < 5){
        DrawCard();
      }
    }

    var i = 0;

    hand.forEach(card => {
      const { rank, suit } = card;
      const cardObj = { rank, suit };
      handToSubmit[i] = cardObj;
      i++;
    });
  };

  $('#shuffle').click(doShuffle);
  $('#drawHand').click(doDrawHand);
  $('#reset').click(reset);
};

$(document).ready(main);
