% We set the random seed for reproducable results. 
rng(42);



datasize = 1000;
% We start be generating a random hyperplane. 
w = [randi([-100 100]) randi([-100 100])];

% Draw the plane
func = @(x) -(w(1)*x/w(2));
x = linspace(-1, 1);
y = func(x);

% Generate random sample data
data = -1 + (1-(-1)).*rand(datasize, 2);

% Create labels for the data
for i = 1 : datasize
    x1 = data(i, 1);
    y1 = data(i, 2);
    if y1 < func(x1)
        labels(i) = -1;
    else
        labels(i) = 1;
    end
end

% Plotting
figure
plot(x, y)
hold on
w = [4 3]
func = @(x) -(w(1)*x/w(2));
plot(x, func(x), '--')

w = w' + labels(11) * data(11,:)'
func1 = @(x) -(w(1)*x/w(2));
plot(x, func1(x), '--')


for i = 1:datasize
    if(labels(i) < 0)
        scatter(data(i,1),data(i,2), 'o', 'green')
    else
        scatter(data(i,1),data(i,2), '+', 'red')
    end
end
        
axis([-1.1,1.1,-1.1,1.1])